import os

# Define a few variables
current_directory = os.path.dirname("__file__")
data_directory = os.path.join(current_directory, "data")
documents_directory = os.path.join(data_directory, "documents")
templates_directory = os.path.join(current_directory, "templates")
group_template = os.path.join(templates_directory, "group.md")


# Download ATT&CK STIX Data
from attackcti.utils.downloader import STIXDownloader

stix20_downloader = STIXDownloader(download_dir="./data/attack", stix_version="2.0")
stix20_downloader.download_all_domains(release="15.1")

print(stix20_downloader.downloaded_file_paths)


# Initialize ATT&CK Python library
from attackcti import attack_client

lift = attack_client(local_paths=stix20_downloader.downloaded_file_paths)

# Get a list of the techniques used across all groups
techniques_used_by_groups = lift.get_techniques_used_by_all_groups()
print(f"\nTechniques: \n{techniques_used_by_groups[0]}")


# Create the ATT&CK groups markdown files
import copy
from jinja2 import Template

# Create Group docs
all_groups = dict()
for technique in techniques_used_by_groups:
    if technique["id"] not in all_groups:
        group = dict()
        group["group_name"] = technique["name"]
        group["group_id"] = technique["external_references"][0]["external_id"]
        group["created"] = technique["created"]
        group["modified"] = technique["modified"]
        group["description"] = technique["description"]
        group["aliases"] = technique["aliases"]
        if "x_mitre_contributors" in technique:
            group["contributors"] = technique["x_mitre_contributors"]
        group["techniques"] = []
        all_groups[technique["id"]] = group
    technique_used = dict()
    technique_used["matrix"] = technique["technique_matrix"]
    technique_used["domain"] = technique["x_mitre_domains"]
    technique_used["platform"] = technique["platform"]
    technique_used["tactics"] = technique["tactic"]
    technique_used["technique_id"] = technique["technique_id"]
    technique_used["technique_name"] = technique["technique"]
    technique_used["use"] = technique["relationship_description"]
    if "data_sources" in technique:
        technique_used["data_sources"] = technique["data_sources"]
    all_groups[technique["id"]]["techniques"].append(technique_used)

if not os.path.exists(documents_directory):
    print("[+] Creating knowledge directory..")
    os.makedirs(documents_directory)

print("[+] Creating markadown files for each group..")
markdown_template = Template(open(group_template).read())
for key in list(all_groups.keys()):
    group = all_groups[key]
    print("  [>>] Creating markdown file for {}..".format(group["group_name"]))
    group_for_render = copy.deepcopy(group)
    markdown = markdown_template.render(
        metadata=group_for_render,
        group_name=group["group_name"],
        group_id=group["group_id"],
    )
    file_name = (group["group_name"]).replace(" ", "_")
    open(f"{documents_directory}/{file_name}.md", encoding="utf-8", mode="w").write(
        markdown
    )

# Load the documents
import glob
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# variables
group_files = glob.glob(os.path.join(documents_directory, "*.md"))

# Loading Markdown files
md_docs = []
print("[+] Loading Group markdown files..")
for group in group_files:
    print(f" [*] Loading {os.path.basename(group)}")
    loader = UnstructuredMarkdownLoader(group)
    md_docs.extend(loader.load())

print(f"[+] Number of .md documents processed: {len(md_docs)}")

# Print a sample page content
print(f"\nSample content:\n\n{md_docs[0].page_content}")


# Recursively split by character
# This text splitter is the recommended one for generic text.
# It is parameterized by a list of characters. It tries to split on them in
# order until the chunks are small enough. The default list is ["\n\n", "\n", " ", ""].
# This has the effect of trying to keep all paragraphs (and then sentences, and then words)
# together as long as possible, as those would generically seem to be the strongest semantically related pieces of text.

from langchain_text_splitters import RecursiveCharacterTextSplitter

import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")


def tiktoken_len(text):
    tokens = tokenizer.encode(
        text, disallowed_special=()  # To disable this check for all special tokens
    )
    return len(tokens)


# Chunking Text
print("[+] Initializing RecursiveCharacterTextSplitter..")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,  # number of tokens overlap between chunks
    add_start_index=True,  # the character index at which each split Document starts within the initial Document is preserved
    length_function=tiktoken_len,
    separators=["\n\n", "\n", " ", ""],
)


print("[+] Splitting documents in chunks..")
chunks = text_splitter.split_documents(md_docs)

print(f"[+] Number of documents: {len(md_docs)}")
print(f"[+] Number of chunks: {len(chunks)}")

print(chunks[0])
print(chunks[1])
print(chunks[2])

# Embed the documents
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS  # , DistanceStrategy

# If you want to define the OpenAI embeddings function
# from langchain_openai import OpenAIEmbeddings

# If you want to define an open-source embedding function
embeddings_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")


# Create or load the database from disk
# https://python.langchain.com/v0.2/docs/integrations/vectorstores/faiss/
from langchain_community.vectorstores.faiss import DistanceStrategy

db_dir = "data/faiss/faiss_index"

# Check if database directory exists
if os.path.exists(db_dir):
    # Load database from disk
    db = FAISS.load_local(
        folder_path=db_dir,
        embeddings=embeddings_function,
        distance_strategy=DistanceStrategy.COSINE,
        allow_dangerous_deserialization=True,
    )
else:
    # With OpenAI Embeddings
    # db = FAISS.from_documents(chunks, OpenAIEmbeddings())

    # Create a new database
    db = FAISS.from_documents(
        chunks, embedding=embeddings_function, distance_strategy=DistanceStrategy.COSINE
    )
    # Sabe database to disk
    db.save_local("data/faiss/faiss_index")


# **********************************************
# query it
query = "What threat actor sends text messages over social media to their targets?"
relevant_docs = db.similarity_search(query)  # query it
# **********************************************

print(f"\n\n\n******* FINAL ANSWER:\n\n")
print(relevant_docs)
