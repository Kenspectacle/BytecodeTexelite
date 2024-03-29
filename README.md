# BytecodeTexelite
Used to process all Java files into .class.bc Java Bytecode files. It works by extracting everything within the jar file, and then copying the class files into another folder, and finally getting the bytecode file.
## Requirement
Java 8+ installed
Python 3 installed
## How to use
1. Use the CompileAllJavaSourceCodes.py and specify which folder to compile the JAR files
2. To be continued
## Unwrapper for XML
This is used for preprocessing the code clone XML output from NiCad before it is used as an input to BigCloneBench. In order to use this, you simply need to run this command in your terminal

 ```
python code_clone_XML_unwrapper.py [code_clone_file] [output file]
 ```

## Bytecode Shortcut Unwrapper
In Bytecode files, it is common to use shortcuts for commonly used JVM instructions, such as aload_0 or aload_1. In the Bytecode shortcut unwrapper, you can unwrap the shortcut, such that the JVM instruction and the operator are separated. To use this, simply run
```
./Bytecode_Shortcut_Unwrapper.sh [target_folder]

```
Warning: This script will replace the original files.