# EmbossFeature.inputFaces Property![](../images/TestTubeLarge.png)

Parent Object: [EmbossFeature](EmbossFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EmbossFeature.h>

## Description

Gets and sets an array of BRepFace objects that define the faces the emboss will be performed on. The value of the isTangentChain property controls if faces that are tangent to any of the specified faces are also included.

## Syntax

* [Python](#Python)
* [C++](#C++)

"embossFeature\_var" is a variable referencing an EmbossFeature object. |

"embossFeature\_var" is a variable referencing an EmbossFeature object. ```` ``` #include <Fusion/Features/EmbossFeature.h>  // Get the value of the property. std::vector<Ptr<BRepFace>> propertyValue = embossFeature_var->inputFaces();  // Set the value of the property, where value_var is a BRepFace. bool returnValue = embossFeature_var->inputFaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [BRepFace](BRepFace.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |