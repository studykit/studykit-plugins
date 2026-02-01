# ConstructionPointInput.creationOccurrence Property

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

In order for geometry to be transformed correctly, an occurrence for creation needs to be specified when the ConstructionPoint is created based on geometry (e.g. a sketch point) in another component AND (the ConstructionPoint) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object. |

"constructionPointInput\_var" is a variable referencing a ConstructionPointInput object. ```` ``` #include <Fusion/Construction/ConstructionPointInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = constructionPointInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = constructionPointInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |