# ConstructionPlaneInput.creationOccurrence Property

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the ConstructionPlane is created based on geometry (e.g. a planarEntity) in another component AND (the ConstructionPlane) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a ConstructionPlaneInput object. |

"constructionPlaneInput\_var" is a variable referencing a ConstructionPlaneInput object. ```` ``` #include <Fusion/Construction/ConstructionPlaneInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = constructionPlaneInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = constructionPlaneInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |