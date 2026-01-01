# ConfigurationReplaceDesigns.add Method

Parent Object: [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesigns.h>

## Description

Adds a new ConfigurationReplaceDesign object to the column. The ConfigurationReplaceDesign objects associated with the column can be used in the cells in the column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationReplaceDesigns\_var" is a variable referencing a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) object.```` ``` returnValue = configurationReplaceDesigns_var.add(name, dataFile) ``` ```` |

"configurationReplaceDesigns\_var" is a variable referencing a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm) | Returns the newly created ConfigurationReplaceDesign. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the new ConfigurationReplaceDesign object. The name must be unique with respect to the other ConfigurationReplaceDesign objects defined for this column. An empty string can be provided, which will cause Fusion to use a default naming scheme to create a name. |
| dataFile | [DataFile](DataFile.htm) | A DataFile object that defines which Design to use. This must be a DataFile object that represents a standard design, not a configured design. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |