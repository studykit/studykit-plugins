# SharedLink.isDownloadAllowed Property

Parent Object: [SharedLink](SharedLink.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/SharedLink.h>

## Description

Specifies if the user with the shared link can download the file or only view it. Changing this setting changes the behavior of the existing link. When a DataFile is shared, and a link is created, this defaults to true, allowing anyone with the link to download the file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedLink\_var" is a variable referencing a SharedLink object. |

"sharedLink\_var" is a variable referencing a SharedLink object. ```` ``` #include <Core/Dashboard/SharedLink.h>  // Get the value of the property. boolean propertyValue = sharedLink_var->isDownloadAllowed();  // Set the value of the property, where value_var is a boolean. bool returnValue = sharedLink_var->isDownloadAllowed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |