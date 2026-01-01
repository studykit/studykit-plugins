# ConfigurationJointSnaps.add Method

Parent Object: [ConfigurationJointSnaps](ConfigurationJointSnaps.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationJointSnaps.h>

## Description

Adds a new snap to the column. The snaps associated with the column can be used in the cells in the column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationJointSnaps\_var" is a variable referencing a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm) object.```` ``` returnValue = configurationJointSnaps_var.add(name, jointGeometry) ``` ```` |

"configurationJointSnaps\_var" is a variable referencing a [ConfigurationJointSnaps](ConfigurationJointSnaps.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationJointSnap](ConfigurationJointSnap.htm) | Returns the newly created ConfigurationJointSnap. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the new snap. The name must be unique with respect to the other snaps defined for this column. An empty string can be provided, which will cause Fusion to use a default naming scheme to create a name. |
| jointGeometry | [Base](Base.htm) | A JointGeometry object that defines how the snap is defined. When creating the JointGeometry object, it must be limited to geometry in the occurrence associated with the column. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |