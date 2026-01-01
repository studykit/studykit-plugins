# SharedLink.isShared Property

Parent Object: [SharedLink](SharedLink.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/SharedLink.h>

## Description

Gets and sets if a shared link should be made available for this DataFile. This property defaults to false for a new DataFile. Setting it to true will allow the URL for the file to be obtained. Setting it to false will restrict access to the URL and block access for anyone currently using it. In other words, this is a dynamic setting and doesn't just control getting the link URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedLink\_var" is a variable referencing a SharedLink object. |

"sharedLink\_var" is a variable referencing a SharedLink object. ```` ``` #include <Core/Dashboard/SharedLink.h>  // Get the value of the property. boolean propertyValue = sharedLink_var->isShared();  // Set the value of the property, where value_var is a boolean. bool returnValue = sharedLink_var->isShared(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |