# ModelAnnotation.GetDisplayGeometry Method

Parent Object: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md)

## Description

Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids.

## Remarks

Below is an example of a feature control symbol. Like most annotations it consists of some geometry and some text. This method only returns the geometry which is shown in black below. You can get the textual information separately in one of two ways, as a description of the text or as graphics that represent the display of the text. As a description of the text you can use properties on the various annotations to determine the text that’s displayed. For the raw text graphics, use the GetDisplayText method.
![](../Images/GetDisplayGeometryExample.png)
For the above example, Below are each of the arguments and the values returned along with a brief description of the value.
GroupCount = 4, In this example each character or symbol is a group, but this shouldn’t be expected in all cases. For example a group defines a filled area and voids within that area. A character that has disjoint filled areas like a percent sign **%** will be returned as three groups since there are three filled areas. Unfilled shapes can be returned as a group of multiple polylines or several groups each containing a single polyline. The geometry described is the same and no expectation should be made about how it’s presented.
**PolylinesPerGroup**
(0) = 2
(1) = 3
(2) = 1
(3) = 3
The number of polylines within each group is specified with this argument, where a polyline is equivalent to a loop.