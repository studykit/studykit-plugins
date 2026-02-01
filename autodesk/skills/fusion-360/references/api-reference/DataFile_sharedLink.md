# DataFile.sharedLink Property

Parent Object: [DataFile](DataFile.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFile.h>

## Description

Returns the SharedLink object associated with this DataFile. You can use the SharedLink object to enable a shared link and set its behavior and to get the shared link URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFile\_var" is a variable referencing a DataFile object. |

"dataFile\_var" is a variable referencing a DataFile object. ```` ``` #include <Core/Dashboard/DataFile.h>  // Get the value of the property. Ptr<SharedLink> propertyValue = dataFile_var->sharedLink(); ``` ```` |

## Property Value

This is a read only property whose value is a [SharedLink](SharedLink.htm).

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |