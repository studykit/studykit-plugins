# Application.scripts Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the Scripts object which provides the ability to manage scripts and add-ins.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<Scripts> propertyValue = application_var->scripts(); ``` ```` |

## Property Value

This is a read only property whose value is a [Scripts](Scripts.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |