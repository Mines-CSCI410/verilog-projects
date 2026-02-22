# Project 5

This project will draw on a lot of your previous work in projects 1 through 3.

You'll need to copy any gates you want to use into this directory for local
tests, and include them with your submission.

Please note, the autograder already has access to `nand.v`, `muxlib.v`, and
`dff.v`. Including these in your submission will cause namespace collisions.

## Indexing into Packed-Vector Representations of Memory

In the `student_computer` and `student_memory` modules, you'll need to access
memory that is represented via a packed vector.
This means it is a single large value instead of many 16-bit values. Indexing
into this takes a little care, since something like `data[16*(i+1):16*i]` will
not work.

Instead, use the following syntax:

```verilog
data[16 * i +: 16]
```

This indicates a 16-bit slice starting at `16 * i`.
