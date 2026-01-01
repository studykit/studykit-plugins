# PatchFeatureInput.creationOccurrence Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

For geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Patch feature is created based on geometry (e.g., a profile, edges, faces) in another component AND (the Patch feature) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. Ptr<Occurrence> propertyValue = patchFeatureInput_var->creationOccurrence();  // Set the value of the property, where value_var is an Occurrence. bool returnValue = patchFeatureInput_var->creationOccurrence(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Occurrence](Occurrence.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |