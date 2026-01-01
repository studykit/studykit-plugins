# ConfigurationReplaceDesigns.itemByName Method

Parent Object: [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesigns.h>

## Description

A method that returns the ConfigurationReplaceDesign object with the specified name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationReplaceDesigns\_var" is a variable referencing a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) object.```` ``` returnValue = configurationReplaceDesigns_var.itemByName(name) ``` ```` |

"configurationReplaceDesigns\_var" is a variable referencing a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm) | Returns the specified ConfigurationReplaceDesign object or null if a ConfigurationReplaceDesign object with the specified name does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the ConfigurationReplaceDesign object to return. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |