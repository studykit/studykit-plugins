# ConfigurationReplaceDesigns.item Method

Parent Object: [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesigns.h>

## Description

A method that returns the specified ConfigurationReplaceDesign object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationReplaceDesigns\_var" is a variable referencing a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) object.```` ``` returnValue = configurationReplaceDesigns_var.item(index) ``` ```` |

"configurationReplaceDesigns\_var" is a variable referencing a [ConfigurationReplaceDesigns](ConfigurationReplaceDesigns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm) | Returns the specified ConfigurationReplaceDesign object or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the ConfigurationReplaceDesign object to return, where the first row is index 0. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |