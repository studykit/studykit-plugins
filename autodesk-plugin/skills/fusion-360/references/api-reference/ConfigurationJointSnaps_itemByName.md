# ConfigurationJointSnaps.itemByName Method

Parent Object: [ConfigurationJointSnaps](ConfigurationJointSnaps.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnaps.h>

## Description

A method that returns the snap with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnaps\_var" is a variable referencing a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm) object.```` ``` returnValue = configurationJointSnaps_var.itemByName(name) ``` ```` |

"configurationJointSnaps\_var" is a variable referencing a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationJointSnap](ConfigurationJointSnap.htm) | Returns the specified snap or null if a snap with the specified name does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the snap to return. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |