import extract
import source

for r in source.get_sources():
    print(r)
    print(extract.extract(r))
