# Arc Raiders Item Image Classifier

simple nerual network to train a model to identify items in Arc Raiders based on an image of the item itself.


## Dataset
used a javascript script to pull all images of items from the arc raiders wiki https://arc-raiders.fandom.com/wiki/Items and save them into a named folder under `arc-raiders-items`

used another python script to create 99 more images of each item with random transformations done to them for dataset diversity and size (as there are only like 100~ items right now)

torchvision datasets ImageFolder takes care of most of the magic converting images -> tensors 

## neural net layout

takes image tensors, flattens to id, then connects 12,288 input features (pixels on images) to 128 hidden layer
not sure what ReLU does yet but it works
dropout increases robustness and reduce overfitting
convert from 128 neurons to amount of classes we have

## export
exported to .pth for load_stat_dict and also onnx for more inference in node?


## why
- learn some ML and neural net stuff
- build this for future project (coming soon)
