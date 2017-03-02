# Simple list comparison script

## Usage

1. [Download][download] and unzip this project to a known folder.
2. Open up your computer's terminal application.
3. Move into the directory and execute script like so:

```
cd path/to/unzipped/arianne-halp-master
python compare_lists.py
# Should output some help text
python compare_lists.py sample_data/file1.txt sample_data/file2.txt
# Should output the common elements

# To put that data in a file instead of printing to your screen:
python compare_lists.py sample_data/file1.txt sample_data/file2.txt > my_common_list.txt
```

## Notes

* Assumes:
  * We're looking for exact matches between lists.
  * List files have one entry per line.


   [download]: https://github.com/patcon/arianne-halp/archive/master.zip
