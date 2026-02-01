# ConstructionAxisInput.creationOccurrence Property

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the ConstructionAxis is created based on geometry (e.g. a straight edge) in another component AND (the ConstructionAxis) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a ConstructionAxisInput object. |

"constructionAxisInput\_var" is a variable referencing a ConstructionAxisInput object. ```` ``` #include <Fusion/Construction/ConstructionAxisInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = constructionAxisInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = constructionAxisInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |