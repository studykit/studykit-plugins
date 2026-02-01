# ConfigurationFeatureAspectColumn.deleteMe Method

Parent Object: [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>

## Description

Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFeatureAspectColumn\_var" is a variable referencing a [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm) object.```` ``` returnValue = configurationFeatureAspectColumn_var.deleteMe() ``` ```` |

"configurationFeatureAspectColumn\_var" is a variable referencing a [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the deletion was successful. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |