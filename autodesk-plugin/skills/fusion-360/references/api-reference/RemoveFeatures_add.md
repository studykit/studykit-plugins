# RemoveFeatures.add Method

Parent Object: [RemoveFeatures](RemoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RemoveFeatures.h>

## Description

Creates a new Remove feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"removeFeatures\_var" is a variable referencing a [RemoveFeatures](RemoveFeatures.htm) object.```` ``` returnValue = removeFeatures_var.add(itemToRemove) ``` ```` |

"removeFeatures\_var" is a variable referencing a [RemoveFeatures](RemoveFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RemoveFeature](RemoveFeature.htm) | Returns the newly created RemoveFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| itemToRemove | [Base](Base.htm) | A single body (solid or surface) or component occurrence to remove. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [removeFeatures.add](removeFeatures_add_Sample.htm) | Demonstrate the removeFeatures.add method. The Remove feature is the same as selecting a body in the browser and selecting "Remove" in the context menu. |
| [Remove Feature](RemoveFeatureSample_Sample.htm) | Demonstrates creating a new remove feature. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |