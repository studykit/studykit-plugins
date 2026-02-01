# RipFeatures.add Method

Parent Object: [RipFeatures](RipFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

Creates a new Rip feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object.```` ``` returnValue = ripFeatures_var.add(input) ``` ```` |

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RipFeature](RipFeature.htm) | Returns the newly created RipFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [RipFeatureInput](RipFeatureInput.htm) | A RipFeatureInput object that defines the desired rip. Use the createInput method to create a new RipFeatureInput object and then use methods on it (the RipFeatureInput object) to define the rip. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |