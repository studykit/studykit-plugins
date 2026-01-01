# ConfigurationReplaceDesign.dataFile Property

Parent Object: [ConfigurationReplaceDesign](ConfigurationReplaceDesign.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationReplaceDesign.h>

## Description

Gets the Design object associated with this ConfigurationReplaceDesign object. This must be a DataFile object that represents a standard design, not a configured design.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationReplaceDesign\_var" is a variable referencing a ConfigurationReplaceDesign object. |

"configurationReplaceDesign\_var" is a variable referencing a ConfigurationReplaceDesign object. ```` ``` #include <Fusion/Configurations/ConfigurationReplaceDesign.h>  // Get the value of the property. Ptr<DataFile> propertyValue = configurationReplaceDesign_var->dataFile(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |