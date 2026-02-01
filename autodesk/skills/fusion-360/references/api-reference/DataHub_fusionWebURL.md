# DataHub.fusionWebURL Property

Parent Object: [DataHub](DataHub.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

Returns a URL that can be used to access the Fusion Web interface for this hub within a browser. The person using the URL must have an Autodesk account and have authority to access the hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHub\_var" is a variable referencing a DataHub object. |

"dataHub\_var" is a variable referencing a DataHub object. ```` ``` #include <Core/Dashboard/DataHub.h>  // Get the value of the property. string propertyValue = dataHub_var->fusionWebURL(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |