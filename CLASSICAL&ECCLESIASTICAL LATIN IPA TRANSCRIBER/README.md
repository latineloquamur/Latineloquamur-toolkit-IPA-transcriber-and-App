# IPA Latin

The IPA Latin tool is a simple application designed by Tommaso Spinelli (Classics) and Giacomo Fenzi (Computer Science) to easily and efficiently compute the IPA phonetic transcription of a given word.

## Compilation
In order to compile this tool, [install Rust](https://rustup.rs/), navigate to this directory, open a command window and run the following:  
``` 
cargo build 
```
The resulting executable will be located at ```target/debug/ipa_latin(.exe)``` where the ```.exe``` will be present only on Windows.

## Usage
Usage is simple, this tool takes as an input a path to a file, which contains a list of words, one per line.
The output will be two files, ```classical.txt``` and ```eccl.txt``` which respectively contain the classical and ecclesiastical transcription of the word.
To run it one can either do (if in the correct working directory):
```
cargo run -- {path to the file}
```
Or:
```
{path to exe} {path to the file} 
```

## Design

The project is conceptually pretty simple. Given an input word, it applies iteratively a number of replacements rules, such as ```ŭ -> ʊ```. The rules are all applied in descending length order, in order to match longer structures such as diphthongs first. 
