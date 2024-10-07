flowchart TD
    A[Start: Full list of computers] --> B{Run script with first half}
    B -->|Success| C[Problem in second half]
    B -->|Failure| D[Problem in first half]
    
    C --> E{Run script with 3/4 of list}
    D --> F{Run script with 1/4 of list}
    
    E -->|Success| G[Problem in last quarter]
    E -->|Failure| H[Problem in third quarter]
    
    F -->|Success| I[Problem in second quarter]
    F -->|Failure| J[Problem in first quarter]
    
    G --> K[Narrow down within last quarter]
    H --> L[Narrow down within third quarter]
    I --> M[Narrow down within second quarter]
    J --> N[Narrow down within first quarter]
    
    K --> O[Problematic computer identified]
    L --> O
    M --> O
    N --> O