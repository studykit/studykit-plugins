# ConfigurationSuppressColumn.feature Property

Parent Object: [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressColumn.h>

## Description

Returns the feature whose suppression state is being controlled by this column. The term "feature" is used broadly and includes anything displayed in the timeline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSuppressColumn\_var" is a variable referencing a ConfigurationSuppressColumn object.  ```` ``` # Get the value of the property. propertyValue = configurationSuppressColumn_var.feature ``` ```` |

"configurationSuppressColumn\_var" is a variable referencing a ConfigurationSuppressColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationSuppressColumn.h>  // Get the value of the property. Ptr<Base> propertyValue = configurationSuppressColumn_var->feature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |