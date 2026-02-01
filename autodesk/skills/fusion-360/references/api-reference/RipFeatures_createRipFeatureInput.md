# RipFeatures.createRipFeatureInput Method

Parent Object: [RipFeatures](RipFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeatures.h>

## Description

Creates a RipFeatureInput object. Use methods on this object to define the rip you want to create and then use the add method, passing in the RipFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object.```` ``` returnValue = ripFeatures_var.createRipFeatureInput() ``` ```` |

"ripFeatures\_var" is a variable referencing a [RipFeatures](RipFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RipFeatureInput](RipFeatureInput.htm) | Returns the newly created RipFeatureInput object or null if the creation failed. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |