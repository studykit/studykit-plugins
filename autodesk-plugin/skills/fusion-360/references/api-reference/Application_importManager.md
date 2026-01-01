# Application.importManager Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the ImportManager. You use the ImportManager to import files (of various neutral formats.) into existing components or new document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<ImportManager> propertyValue = application_var->importManager(); ``` ```` |

## Property Value

This is a read only property whose value is an [ImportManager](ImportManager.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |