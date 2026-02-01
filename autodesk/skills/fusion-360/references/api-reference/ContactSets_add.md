# ContactSets.add Method

Parent Object: [ContactSets](ContactSets.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ContactSets.h>

## Description

Creates a new contact set for the provided occurrences and/or bodies.

## Syntax

* [Python](#Python)
* [C++](#C++)

"contactSets\_var" is a variable referencing a [ContactSets](ContactSets.htm) object.```` ``` returnValue = contactSets_var.add(occurrencesAndBodies) ``` ```` |

"contactSets\_var" is a variable referencing a [ContactSets](ContactSets.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ContactSet](ContactSet.htm) | Returns the newly created ContactSet or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrencesAndBodies | Base[] | An array of Occurrence or BRepBody objects that will be included in the contact set. All occurrences and bodies must be in the context of the root component. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SliderJointMotion API Sample](SliderJointMotionSample_Sample.htm) | Demonstrates creating a joint with slider joint motion. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |