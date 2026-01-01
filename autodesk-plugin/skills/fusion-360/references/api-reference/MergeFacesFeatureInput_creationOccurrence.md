# MergeFacesFeatureInput.creationOccurrence Property

Parent Object: [MergeFacesFeatureInput](MergeFacesFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatureInput.h>

## Description

In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Merge is created based on geometry (e.g. faces) in another component AND (Merge) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. |

"mergeFacesFeatureInput\_var" is a variable referencing a MergeFacesFeatureInput object. ```` ``` #include <Fusion/Features/MergeFacesFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = mergeFacesFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = mergeFacesFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |