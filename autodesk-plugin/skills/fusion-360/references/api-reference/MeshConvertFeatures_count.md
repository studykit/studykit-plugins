# MeshConvertFeatures.count Property![](../images/TestTubeLarge.png)

Parent Object: [MeshConvertFeatures](MeshConvertFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshConvertFeatures.h>

## Description

The number of mesh convert features in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshConvertFeatures\_var" is a variable referencing a MeshConvertFeatures object. |

"meshConvertFeatures\_var" is a variable referencing a MeshConvertFeatures object. ```` ``` #include <Fusion/MeshBody/MeshConvertFeatures.h>  // Get the value of the property. uinteger propertyValue = meshConvertFeatures_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |