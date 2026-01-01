# ConfigurationJointSnaps.item Method

Parent Object: [ConfigurationJointSnaps](ConfigurationJointSnaps.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnaps.h>

## Description

A method that returns the specified snap using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnaps\_var" is a variable referencing a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm) object.```` ``` returnValue = configurationJointSnaps_var.item(index) ``` ```` |

"configurationJointSnaps\_var" is a variable referencing a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationJointSnap](ConfigurationJointSnap.htm) | Returns the specified snap or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the snap to return, where the first row is index 0. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |