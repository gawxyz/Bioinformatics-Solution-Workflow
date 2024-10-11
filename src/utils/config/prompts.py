# 工具类型列表
TOOL_TYPE_LIST = """
{
  "Algorithm": "A set of computational steps and rules in bioinformatics used to solve specific problems, including general algorithms and machine learning algorithms. Examples include sequence alignment algorithms and clustering algorithms.",
  
  "Command-line tool": "A tool operated through a text-based command-line interface, often used for task automation and batch processing.",
  
  "Database portal": "A web application or workbench providing access to biological databases.",
  
  "Desktop application": "Software with a graphical user interface that runs in a local environment, such as personal computers or mobile devices.",
  
  "Library": "A collection of components used to construct other tools, focusing on high-level bioinformatics functions. Does not include low-level programming libraries.",
  
  "Method": "A systematic strategy for analyzing biological data, often combining multiple tools and steps. Suitable for describing specific experimental designs or data analysis processes.",
  
  "Model": "A conceptual or computational framework used to represent, simulate, predict, or analyze biological systems or processes. In the context of AI, it refers to models using machine learning or deep learning algorithms to automate bioinformatics tasks.",
  
  "Ontology": "A structured collection of information about concepts in a specific domain, including terms, synonyms, and descriptions.",
  
  "Plug-in": "A software component encapsulating related functions that depend on other software for use, such as JavaScript widgets or extensions that enhance existing tool functionality.",
    
  "Suite": "A collection of related tools bundled together, typically sharing functionality, user interface, and data exchange capabilities. Includes collections of standalone command-line tools or web applications within a common portal.",
  
  "Web application": "A tool with a graphical user interface that runs in a web browser.",
  
  "Web API": "An application programming interface (API) consisting of endpoints for a request-response message system accessible via HTTP. Ranges from simple data-access URLs to RESTful APIs.",
  
  "Workbench": "An application or suite with a graphical user interface, providing an integrated environment for data analysis. It may include or be extended with various functions or tools. Encompasses workflow systems, platforms, and frameworks.",

  "Workflow": "A set of tools composed into a processing pipeline, typically standalone but combined for convenience, often for batch execution via a workflow engine or script."
}
"""
# 工具类型简表
TOOL_TYPE_LIST_SIMPLE = "['Algorithm', 'Command-line tool', 'Database portal', 'Desktop application', 'Library', 'Method', 'Model', 'Ontology', 'Plug-in', 'Suite', 'Web application', 'Web API', 'Workbench', 'Workflow']"

# 生物科学主题列表
BIOSCIENCE_TOPIC_LIST = """
{
    "Biology": {
        "Agricultural science": "Multidisciplinary study, research and development within the field of agriculture.",
        "Biochemistry": "Chemical substances and physico-chemical processes that occur within living organisms.",
        "Biomarkers": "Objective indicators of biological state often used to assess health, and determinate treatment.",
        "Biophysics": "The use of physics to study biological systems.",
        "Biotechnology": "The exploitation of biological process, structure and function for industrial purposes.",
        "Cell biology": "Cells, such as key genes and proteins involved in the cell cycle.",
        "Chemical biology": "The use of synthetic chemistry to study and manipulate biological systems.",
        "Developmental biology": "How organisms grow and develop.",
        "Evolutionary biology": "The evolutionary processes, from the genetic to environmental scale, that produced life in all its diversity.",
        "Freshwater biology": "The study of organisms in freshwater ecosystems.",
        "Genetics": "The study of genes, genetic variation and heredity in living organisms.",
        "Human biology": "The study of human beings in general, including the human genome and proteome.",
        "Marine biology": "The study of organisms in the ocean or brackish waters.",
        "Microbiology": "The biology of microorganisms.",
        "Model organisms": "Specific organisms used to study biological processes, often involving genomic or proteomic analysis.",
        "Molecular biology": "The molecular basis of biological activity, particularly macromolecules essential to life.",
        "Plant biology": "The study of plants, including specific plant genomes and molecular sequences.",
        "Structural biology": "Experimental methods for biomolecular structure determination and molecular structure analysis.",
        "Synthetic biology": "The application of multi-disciplinary science to construct artificial biological systems for various applications.",
        "Systems biology": "The holistic modelling and analysis of complex biological systems and their interactions.",
        "Virology": "The study of viruses, including sequence and structural data, viral proteins, and viral genomes.",
        "Zoology": "The study of the animal kingdom, including information on animal genomes and molecular sequences."
    },
    "Biomedical science": {
        "Anatomy": "The form and function of the structures of living organisms.",
        "Immunology": "The application of information technology to immunology, including immunological genes and processes.",
        "Laboratory animal science": "The use of animals and alternatives in experimental research.",
        "Medicines research and development": "The discovery, development, and approval of medicines.",
        "Neurobiology": "The study of the nervous system and brain, including anatomy and physiology.",
        "Nutritional science": "The study of the effects of food components on metabolism, health, and disease resistance.",
        "Parasitology": "The biology of parasites.",
        "Pharmacology": "The study of drugs and their effects or responses in living systems.",
        "Regenerative medicine": "Biomedical approaches to clinical interventions that involve the use of stem cells.",
        "Sample collections": "Biological samples and specimens."
    },
    "Computational biology": {
        "Biomolecular simulation": "The study and simulation of molecular conformations using computational models.",
        "Function analysis": "The study of gene and protein function, including the prediction of functional properties of proteins.",
        "Molecular genetics": "The structure and function of genes at the molecular level.",
        "Molecular interactions, pathways and networks": "Molecular interactions, biological pathways, networks, and other models.",
        "Nucleic acids": "Study of nucleic acids, including methods for DNA sequence analysis and phylogenetics.",
        "Phylogeny": "The study of evolutionary relationships among organisms, including phylogenetic tree construction.",
        "Proteins": "Archival, processing, and analysis of protein data, including molecular sequences and structural data.",
        "Sequence analysis": "The archival, processing, and analysis of molecular sequences, including sequence sites, alignments, motifs, and profiles.",
        "Sequence sites, features and motifs": "The detection and analysis of positional features in molecular sequences.",
        "Structure analysis": "The curation, processing, and prediction of the structure of biological molecules."
    },
    "Ecology": {
        "Biodiversity": "The degree of variation of life forms within a given ecosystem or planet.",
        "Carbon cycle": "The biogeochemical pathway of carbon moving through Earth's systems.",
        "Metagenomics": "The study of genetic material recovered from environmental samples, often combined with environmental data.",
        "Microbial ecology": "The ecology of microorganisms, including their relationships with each other and the environment."
    },
    "Medicine": {
        "Allergy, clinical immunology and immunotherapeutics": "Health issues related to the immune system and their prevention, diagnosis, and management.",
        "Anaesthesiology": "Anaesthesia and anaesthetics.",
        "Cardiology": "The diseases and abnormalities of the heart and circulatory system.",
        "Complementary medicine": "Medical therapies that fall beyond the scope of conventional medicine but may be used alongside it.",
        "Critical care medicine": "The multidisciplinary care of patients with acute, life-threatening illness or injury.",
        "Dentistry": "The study, diagnosis, and treatment of disorders of the oral cavity and maxillofacial area.",
        "Dermatology": "The branch of medicine dealing with prevention, diagnosis, and treatment of skin, hair, and nail disorders.",
        "Ear, nose and throat medicine": "The branch of medicine dealing with disorders of the ear, nose, and throat.",
        "Endocrinology and metabolism": "The branch of medicine dealing with diseases of endocrine organs and pathways of glucose and lipid metabolism.",
        "Gastroenterology": "The branch of medicine dealing with disorders of the gastrointestinal system.",
        "Gender medicine": "The study of biological and physiological differences between males and females and how they affect disease presentation and management.",
        "Geriatric medicine": "The diagnosis, treatment, and prevention of diseases in older people.",
        "Gynaecology and obstetrics": "The health of the female reproductive system, pregnancy, and birth.",
        "Haematology": "The branch of medicine dealing with blood and blood diseases.",
        "Hepatic and biliary medicine": "The branch of medicine dealing with the liver, gallbladder, bile ducts, and bile.",
        "Medical toxicology": "The diagnosis, management, and prevention of poisoning and adverse health effects from toxins.",
        "Musculoskeletal medicine": "The prevention, diagnosis, and treatment of disorders of muscle, bone, and connective tissue.",
        "Neurology": "The branch of medicine dealing with the nervous system and brain.",
        "Oncology": "The study of cancer, including genes and proteins implicated in cancer.",
        "Ophthalmology": "The branch of medicine dealing with disorders of the eye.",
        "Paediatrics": "The medical care of infants, children, and adolescents.",
        "Pain medicine": "The prevention, evaluation, and treatment of persons in pain.",
        "Pathology": "The study of diseases, including genes and proteins involved in diseases.",
        "Personalised medicine": "An approach to medicine tailored to the individual based on predicted response or risk of disease.",
        "Physiology": "The functions of living organisms and their parts.",
        "Psychiatry": "The management of mental illness, emotional disturbance, and abnormal behaviour.",
        "Public health and epidemiology": "The patterns, causes, and effects of disease in populations.",
        "Reproductive health": "The health of the reproductive processes at all stages of life.",
        "Respiratory medicine": "The study of the respiratory system.",
        "Surgery": "The use of operative techniques to treat disease or improve bodily function.",
        "Systems medicine": "An interdisciplinary study of the dynamic systems of the human body.",
        "Toxicology": "The study of toxins and their adverse effects on living organisms.",
        "Translational medicine": "The translation of research into better diagnostic tools, medicines, and procedures.",
        "Trauma medicine": "The branch of medicine that treats body wounds or shock from sudden physical injury.",
        "Tropical medicine": "The study of diseases occurring in tropical regions.",
        "Urology and nephrology": "The study of the urinary system, male reproductive system, and kidney function.",
        "Veterinary medicine": "The branch of medicine dealing with disease and injury in animals."
    },
    "Omics": {
        "Fluxomics": "The complete set of metabolic fluxes in a cell, a dynamic aspect of phenotype.",
        "Genomics": "The study of whole genomes, including genome projects and gene names.",
        "Immunomics": "The study of the immune system, its regulation, and response to pathogens.",
        "Metabolomics": "The systematic study of metabolites and the chemical processes they are involved in.",
        "Molecular evolution": "The study of the process and mechanisms of biomolecular change across generations.",
        "Multiomics": "The integration of data from multiple omics, such as transcriptomics and proteomics.",
        "Phenomics": "The study of phenotypic changes in response to genetic and environmental factors.",
        "Proteomics": "The study of proteins, including their identification and structural analysis."
    }
}
"""

# 生物科学主题简表
BIOSCIENCE_TOPIC_LIST_SIMPLE = ["Agricultural science","Biochemistry","Biomarkers","Biophysics","Biotechnology","Cell biology","Chemical biology","Developmental biology","Evolutionary biology","Freshwater biology","Genetics","Human biology","Marine biology","Microbiology","Model organisms","Molecular biology","Plant biology","Structural biology","Synthetic biology","Systems biology","Virology","Zoology","Anatomy","Immunology","Laboratory animal science","Medicines research and development","Neurobiology","Nutritional science","Parasitology","Pharmacology","Regenerative medicine","Sample collections","Biomolecular simulation","Function analysis","Molecular genetics","Molecular interactions, pathways and networks","Nucleic acids","Phylogeny","Proteins","Sequence analysis","Sequence sites, features and motifs","Structure analysis","Biodiversity","Carbon cycle","Metagenomics","Microbial ecology","Allergy, clinical immunology and immunotherapeutics","Anaesthesiology","Cardiology","Complementary medicine","Critical care medicine","Dentistry","Dermatology","Ear, nose and throat medicine","Endocrinology and metabolism","Gastroenterology","Gender medicine","Geriatric medicine","Gynaecology and obstetrics","Haematology","Hepatic and biliary medicine","Medical toxicology","Musculoskeletal medicine","Neurology","Oncology","Ophthalmology","Paediatrics","Pain medicine","Pathology","Personalised medicine","Physiology","Psychiatry","Public health and epidemiology","Reproductive health","Respiratory medicine","Surgery","Systems medicine","Toxicology","Translational medicine","Trauma medicine","Tropical medicine","Urology and nephrology","Veterinary medicine","Fluxomics","Genomics","Immunomics","Metabolomics","Molecular evolution","Multiomics","Phenomics","Proteomics"]

# 论文摘要提示模板
SUMMARY_PAPER_TEMPLATE = """You are an advanced AI trained to analyze scientific papers from PubMed Central. Your task is to extract key information from the provided JSON content of a full-text article and generate a structured JSON summary.

Carefully analyze the following JSON content of a scientific paper:

{paper_content}

Based on this JSON content, create a JSON summary with the following structure:

{{
  "description": "A concise description of the main focus and findings of the paper (2-3 sentences)",
  "function": "A detailed explanation of the main contributions, methodologies, or tools presented in the paper",
  "homepage": "The official website or repository of any tool or software mentioned in the paper, if available",
  "keywords": "The keywords of the paper"
}}

Guidelines:
1. Extract information from relevant JSON keys.
2. The "description" should provide a quick overview of the paper's main points.
3. The "function" field should elaborate on the paper's key contributions, methods, or tools.
4. If a homepage is not explicitly mentioned, you may leave it as an empty string.
6. If any field cannot be confidently filled based on the provided JSON content, use null as the value.

Please provide the JSON summary based on the JSON content."""
TOOL_TYPE_PROMPT_TEMPLATE = """You are a software engineer tasked with classifying software tools. \n

    Here are the definitions of the tool types: \n\n {tool_type_list} \n\n 
    Here is the paper of the tool: \n\n {paper_content} \n\n
    Classify the tools based on the definitions, allowing for multiple types per tool.\n
    Provide a JSON format with a single key for the "toolType", like {{"toolType": ["type1", "type2", ...]}}, without any premable or explanations."""
TOOL_TOPIC_PROMPT_TEMPLATE = """You are a life scientist tasked with assigning relevant bioscience topics to a paper. \n
    Here are the concepts of each bioscience topic: \n\n {bioscience_topic_list} \n\n
    Here is the paper's content: \n\n {paper_content} \n\n
    Assign the main relevant scientific topics based on the provided bioscience concepts, allowing for multiple topics per paper. \n
    Provide a JSON format with a single key for "Topic", like {{"Topic": ["topic1", "topic2", ...]}}, without any premable or explanations."""