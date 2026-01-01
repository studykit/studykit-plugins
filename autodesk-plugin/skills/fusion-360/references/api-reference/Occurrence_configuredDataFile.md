# Occurrence.configuredDataFile Property

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Returns the DataFile object that represents the specific version of the design used by this occurrence. From the DataFile you can access other version of the file, most importantly, you can access the latest version and get the top configuration table from it.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an Occurrence object. |

"occurrence\_var" is a variable referencing an Occurrence object. ```` ``` #include <Fusion/Components/Occurrence.h>  // Get the value of the property. Ptr<DataFile> propertyValue = occurrence_var->configuredDataFile(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |