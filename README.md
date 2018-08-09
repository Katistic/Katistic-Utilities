# KatisticUtils.py
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
Client = ku.youtube.Init(Key)

ku.youtube.search_list(Client, VideoToSearch, mResults = 10)
```
