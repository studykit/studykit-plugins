# DataHub.hubType Property

Parent Object: [DataHub](DataHub.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHub.h>

## Description

Gets if this hub is a Personal (PersonalHubType) or Team (TeamHubType) type hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHub\_var" is a variable referencing a DataHub object. |

"dataHub\_var" is a variable referencing a DataHub object. ```` ``` #include <Core/Dashboard/DataHub.h>  // Get the value of the property. HubTypes propertyValue = dataHub_var->hubType(); ``` ```` |

## Property Value

This is a read only property whose value is a [HubTypes](HubTypes.htm).

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |