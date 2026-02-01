# Application.applicationFolders Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the ApplicationFolders object which provides access to the paths of various folders associated with Fusion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<ApplicationFolders> propertyValue = application_var->applicationFolders(); ``` ```` |

## Property Value

This is a read only property whose value is an [ApplicationFolders](ApplicationFolders.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |