# UnstitchFeature.inputFaces Property

Parent Object: [UnstitchFeature](UnstitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UnstitchFeature.h>

## Description

Gets the faces that were input to be unstitched.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object.  ```` ``` # Get the value of the property. propertyValue = unstitchFeature_var.inputFaces ``` ```` |

"unstitchFeature\_var" is a variable referencing a UnstitchFeature object. ```` ``` #include <Fusion/Features/UnstitchFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = unstitchFeature_var->inputFaces(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |