# DataEventArgs.file Property

Parent Object: [DataEventArgs](DataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEventArgs.h>

## Description

Gets the DataFile object associated with this event. If there isn't a DataFile associated with the event, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. |

"dataEventArgs\_var" is a variable referencing a DataEventArgs object. ```` ``` #include <Core/Dashboard/DataEventArgs.h>  // Get the value of the property. Ptr<DataFile> propertyValue = dataEventArgs_var->file(); ``` ```` |

## Property Value

This is a read only property whose value is a [DataFile](DataFile.htm).

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |