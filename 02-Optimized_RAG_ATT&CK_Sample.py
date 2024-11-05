from langchain_core.documents import Document


# Create and add metadata to documents

# Creating list of documents
techniques = [
    Document(
        page_content="An adversary may abuse configurations where an application has the setuid or setgid bits set in order to get code running in a different (and possibly more privileged) user's context. On Linux or macOS, when the setuid or setgid bits are set for an application binary, the application will run with the privileges of the owning user or group respectively. Normally an application is run in the current user's context, regardless of which user or group owns the application. However, there are instances where programs need to be executed in an elevated context to function properly, but the user running them may not have the specific required privileges. Instead of creating an entry in the sudoers file, which must be done by root, any user can specify the setuid or setgid flag to be set for their own applications (i.e. Linux and Mac File and Directory Permissions Modification). The chmod command can set these bits with bitmasking, chmod 4777 [file] or via shorthand naming, chmod u+s [file]. This will enable the setuid bit. To enable the setgid bit, chmod 2775 and chmod g+s can be used. Adversaries can use this mechanism on their own malware to make sure they're able to execute in elevated contexts in the future.[2] This abuse is often part of a 'shell escape' or other actions to bypass an execution environment with restricted permissions. Alternatively, adversaries may choose to find and target vulnerable binaries with the setuid or setgid bits already enabled (i.e. File and Directory Discovery). The setuid and setguid bits are indicated with an 's' instead of an 'x' when viewing a file's attributes via ls -l. The find command can also be used to search for such files. For example, find / -perm +4000 2>/dev/null can be used to find files with setuid set and find / -perm +2000 2>/dev/null may be used for setgid. Binaries that have these bits set may then be abused by adversaries.",
        metadata={
            "name": "Setuid and Setgid",
            "id": "T1548.001",
            "tactic": "Privilege Escalation, Defense Evasion",
            "platform": "['Linux', 'macOS']",
        },
    ),
    Document(
        page_content="Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user for confirmation. The impact to the user ranges from denying the operation under high enforcement to allowing the user to perform the action if they are in the local administrators group and click through the prompt or allowing them to enter an administrator password to complete the action. If the UAC protection level of a computer is set to anything but the highest level, certain Windows programs can elevate privileges or execute some elevated Component Object Model objects without prompting the user through the UAC notification box.[2][3] An example of this is use of Rundll32 to load a specifically crafted DLL which loads an auto-elevated Component Object Model object and performs a file operation in a protected directory which would typically require elevated access. Malicious software may also be injected into a trusted process to gain elevated privileges without prompting a user. Many methods have been discovered to bypass UAC. The Github readme page for UACME contains an extensive list of methods that have been discovered and implemented, but may not be a comprehensive list of bypasses. Additional bypass methods are regularly discovered and some used in the wild, such as: eventvwr.exe can auto-elevate and execute a specified binary or script. Another bypass is possible through some lateral movement techniques if credentials for an account with administrator privileges are known, since UAC is a single system security mechanism, and the privilege or integrity of a process running on one system will be unknown on remote systems and default to high integrity.",
        metadata={
            "name": "Bypass User Account Control",
            "id": "T1548.002",
            "tactic": "Privilege Escalation,Defense Evasion",
            "platform": "Windows",
        },
    ),
    Document(
        page_content="Adversaries may perform sudo caching and/or use the sudoers file to elevate privileges. Adversaries may do this to execute commands as other users or spawn processes with higher privileges. Within Linux and MacOS systems, sudo (sometimes referred to as 'superuser do') allows users to perform commands from terminals with elevated privileges and to control who can perform these commands on the system. The sudo command 'allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments.' Since sudo was made for the system administrator, it has some useful configuration features such as a timestamp_timeout, which is the amount of time in minutes between instances of sudo before it will re-prompt for a password. This is because sudo has the ability to cache credentials for a period of time. Sudo creates (or touches) a file at /var/db/sudo with a timestamp of when sudo was last run to determine this timeout. Additionally, there is a tty_tickets variable that treats each new tty (terminal session) in isolation. This means that, for example, the sudo timeout of one tty will not affect another tty (you will have to type the password again). The sudoers file, /etc/sudoers, describes which users can run which commands and from which terminals. This also describes which commands users can run as other users or groups. This provides the principle of least privilege such that users are running in their lowest possible permissions for most of the time and only elevate to other users or permissions as needed, typically by prompting for a password. However, the sudoers file can also specify when to not prompt users for passwords with a line like user1 ALL=(ALL) NOPASSWD: ALL. Elevated privileges are required to edit this file though. Adversaries can also abuse poor configurations of these mechanisms to escalate privileges without needing the user's password. For example, /var/db/sudo's timestamp can be monitored to see if it falls within the timestamp_timeout range. If it does, then malware can execute sudo commands without needing to supply the user's password. Additional, if tty_tickets is disabled, adversaries can do this from any tty for that user. In the wild, malware has disabled tty_tickets to potentially make scripting easier by issuing echo 'Defaults !tty_tickets' >> /etc/sudoers. In order for this change to be reflected, the malware also issued killall Terminal. As of macOS Sierra, the sudoers file has tty_tickets enabled by default.",
        metadata={
            "name": "Sudo and Sudo Caching",
            "id": "T1548.003",
            "tactic": "Privilege Escalation, Defense Evasion",
            "platform": "Linux, macOS",
        },
    ),
    Document(
        page_content="Adversaries may leverage the AuthorizationExecuteWithPrivileges API to escalate privileges by prompting the user for credentials. The purpose of this API is to give application developers an easy way to perform operations with root privileges, such as for application installation or updating. This API does not validate that the program requesting root privileges comes from a reputable source or has been maliciously modified. Although this API is deprecated, it still fully functions in the latest releases of macOS. When calling this API, the user will be prompted to enter their credentials but no checks on the origin or integrity of the program are made. The program calling the API may also load world writable files which can be modified to perform malicious behavior with elevated privileges. Adversaries may abuse AuthorizationExecuteWithPrivileges to obtain root privileges in order to install malicious software on victims and install persistence mechanisms. This technique may be combined with Masquerading to trick the user into granting escalated privileges to malicious code. This technique has also been shown to work by modifying legitimate programs present on the machine that make use of this API.",
        metadata={
            "name": "Elevated Execution with Prompt",
            "id": "T1548.004",
            "tactic": "Privilege Escalation, Defense Evasion",
            "platform": "macOS",
        },
    ),
    Document(
        page_content="Adversaries may abuse permission configurations that allow them to gain temporarily elevated access to cloud resources. Many cloud environments allow administrators to grant user or service accounts permission to request just-in-time access to roles, impersonate other accounts, pass roles onto resources and services, or otherwise gain short-term access to a set of privileges that may be distinct from their own. Just-in-time access is a mechanism for granting additional roles to cloud accounts in a granular, temporary manner. This allows accounts to operate with only the permissions they need on a daily basis, and to request additional permissions as necessary. Sometimes just-in-time access requests are configured to require manual approval, while other times the desired permissions are automatically granted. Account impersonation allows user or service accounts to temporarily act with the permissions of another account. For example, in GCP users with the iam.serviceAccountTokenCreator role can create temporary access tokens or sign arbitrary payloads with the permissions of a service account, while service accounts with domain-wide delegation permission are permitted to impersonate Google Workspace accounts. In Exchange Online, the ApplicationImpersonation role allows a service account to use the permissions associated with specified user accounts. Many cloud environments also include mechanisms for users to pass roles to resources that allow them to perform tasks and authenticate to other services. While the user that creates the resource does not directly assume the role they pass to it, they may still be able to take advantage of the role's access -- for example, by configuring the resource to perform certain actions with the permissions it has been granted. In AWS, users with the PassRole permission can allow a service they create to assume a given role, while in GCP, users with the iam.serviceAccountUser role can attach a service account to a resource. While users require specific role assignments in order to use any of these features, cloud administrators may misconfigure permissions. This could result in escalation paths that allow adversaries to gain access to resources beyond what was originally intended. Note: this technique is distinct from Additional Cloud Roles, which involves assigning permanent roles to accounts rather than abusing existing permissions structures to gain temporarily elevated access to resources. However, adversaries that compromise a sufficiently privileged account may grant another account they control Additional Cloud Roles that would allow them to also abuse these features. This may also allow for greater stealth than would be had by directly using the highly privileged account, especially when logs do not clarify when role impersonation is taking place.",
        metadata={
            "name": "Temporary Elevated Cloud Access",
            "id": "T1548.005",
            "tactic": "Privilege Escalation, Defense Evasion",
            "platform": "Azure AD, Google Workspace, IaaS, Office 365",
        },
    ),
    Document(
        page_content="Adversaries can manipulate or abuse the Transparency, Consent, & Control (TCC) service or database to execute malicious applications with elevated permissions. TCC is a Privacy & Security macOS control mechanism used to determine if the running process has permission to access the data or services protected by TCC, such as screen sharing, camera, microphone, or Full Disk Access (FDA). When an application requests to access data or a service protected by TCC, the TCC daemon (tccd) checks the TCC database, located at /Library/Application Support/com.apple.TCC/TCC.db (and ~/ equivalent), for existing permissions. If permissions do not exist, then the user is prompted to grant permission. Once permissions are granted, the database stores the application's permissions and will not prompt the user again unless reset. For example, when a web browser requests permissions to the user's webcam, once granted the web browser may not explicitly prompt the user again. Adversaries may manipulate the TCC database or otherwise abuse the TCC service to execute malicious content. This can be done in various ways, including using privileged system applications to execute malicious payloads or manipulating the database to grant their application TCC permissions. For example, adversaries can use Finder, which has FDA permissions by default, to execute malicious AppleScript while preventing a user prompt. For a system without System Integrity Protection (SIP) enabled, adversaries have also manipulated the operating system to load an adversary controlled TCC database using environment variables and Launchctl. Adversaries may also opt to instead inject code (e.g., Process Injection) into targeted applications with the desired TCC permissions.",
        metadata={
            "name": "TCC Manipulation",
            "id": "T1548.006",
            "tactic": "Privilege Escalation, Defense Evasion",
            "platform": "macOS",
        },
    ),
]


# Split the documents
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-3.5-turbo")


def tiktoken_len(text):
    tokens = tokenizer.encode(
        text, disallowed_special=()  # To disable this check for all special tokens
    )
    return len(tokens)


from langchain.text_splitter import RecursiveCharacterTextSplitter

doc_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
    length_function=tiktoken_len,
    separators=["\n\n", "\n", ", ", " ", ""],
    add_start_index=True,
)

docs = doc_splitter.split_documents(techniques)

print("There are ", len(docs), " docs")


def nicePrint(listOfDocs):

    for i, doc in enumerate(listOfDocs):

        print(f"Document {i}:\n{doc.page_content}\n")

        print(f"Metadata: {doc.metadata}\n")

        print("=" * 50)


nicePrint(docs)


# Initialize Embedding function

# If you want to define the OpenAI embeddings function
# from langchain_openai import OpenAIEmbeddings

# If you want to define an open-source embedding function
from langchain_huggingface import HuggingFaceEmbeddings

embeddings_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# Equivalent to SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Embed the documents
from langchain_community.vectorstores import FAISS, DistanceStrategy

vectorstore = FAISS.from_documents(
    docs, embedding=embeddings_function, distance_strategy=DistanceStrategy.EUCLIDEAN
)

#####################################################
# Retrieval using Similarity search
#####################################################
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
prompt = "What platform does the Transparency, Consent, & Control (TCC) technique target, macOS or Windows?"
nicePrint(retriever.invoke(input=prompt))


#####################################################
# Retrieval using Metadata Filtering (Pre-Retrieval)
#####################################################
retriever2 = vectorstore.as_retriever(
    search_kwargs={"k": 10, "filter": {"platform": "macOS"}}
)
nicePrint(retriever2.invoke(input=prompt))

#####################################################
# Retrieval using Rerankers
#####################################################
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank

# FlashRank is the Ultra-lite & Super-fast Python library to add re-ranking to your existing search & retrieval pipelines. It is based on SoTA cross-encoders.
# Cross-encoders are more accurate than bi-encoders but they don"t scale well, so using them to re-order a shortened list returned by semantic search is the ideal use case.

FlashrankRerank.update_forward_refs()  # Ensure that FlashrankRerank is correctly defined and update forward references if needed

compressor = FlashrankRerank(
    model="ms-marco-MultiBERT-L-12", top_n=6
)  # default model is: DEFAULT_MODEL_NAME = "ms-marco-MultiBERT-L-12" available models: https://huggingface.co/prithivida/flashrank/tree/main

re_rank_retriever = ContextualCompressionRetriever(
    base_compressor=compressor, base_retriever=retriever  # naive retrieval
)

#####################################################
# Retrieval using Multi-hop
#####################################################
from langchain.retrievers.multi_query import MultiQueryRetriever
import logging
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig()
openai_api_key = os.environ.get("OPEAI_API_KEY")


# Initialize the LLM
llm = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key, temperature=0)

# Define the Retriever
multi_query_retriever = MultiQueryRetriever.from_llm(llm=llm, retriever=retriever)

#####################################################
# Retrieve relevant documents by generating multiple prompts
#####################################################
prompt = "What technique targets macOS systems, 'Bypass User Account Control' or 'Transparency, Consent, & Control (TCC)'?"
multihop_docs = multi_query_retriever.invoke(input=prompt)

nicePrint(multihop_docs)


# Defining augmented prompt
relevantContext = "\n\n".join([doc.page_content for doc in multihop_docs])
augmentedPrompt = f"Question: {prompt} \n\nContext: {relevantContext}"
print(augmentedPrompt)


# Processing Augmented Prompt
response = llm.invoke(input=augmentedPrompt)

print(response.content)
