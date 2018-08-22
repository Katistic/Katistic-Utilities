# Katistic Utilities
Some python utils that I made that I think are useful

## Submodules

Some modules aren't loaded as they require other, external dependancies... These modules have to be imported using ImportOtherSubmodule function.

For example, if you wanted to import the youtube module, which has youtubes python api wrapper as a dependancy
You would do

```python
import katisticutils as ku

YoutubeDevKey = "Key"
VideoToSearch = "Video Title"

ku.ImportOtherSubmodule("youtube")
```
You can then reference the module as normal

```python
Client = ku.youtube.Init(Key)

Results = ku.youtube.search_list(Client, VideoToSearch, mResults = 10)
```

### Current Submodules

* youtube
