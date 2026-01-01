# ConfigurationVisibilityColumn.entity Property

Parent Object: [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityColumn.h>

## Description

Returns the entity whose visibility is being controlled by this column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationVisibilityColumn_var.entity ``` ```` |

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityColumn.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationVisibilityColumn_var->entity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |