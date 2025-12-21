# DerivedAssemblyDefinition.SetHolePatchingOptions Method

Parent Object: [DerivedAssemblyDefinition](../DerivedAssemblyDefinition/DerivedAssemblyDefinition.md)

## Description

Method that sets the hole patching options for the derived assembly.

## Syntax

DerivedAssemblyDefinition.**SetHolePatchingOptions**( ***HolePatchType*** As [DerivedHolePatchEnum](../DerivedHolePatchEnum.md), [***MinimumPerimeter***] As Double, [***MaximumPerimeter***] As Double, [***Reserved***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| HolePatchType | [DerivedHolePatchEnum](../DerivedHolePatchEnum.md) | Input DerivedHolePatchEnum that specifies the holes to patch. Valid values are kDerivedPatchNone, kDerivedPatchAll and kDerivedPatchRange. If kDerivedPatchRange is provided, the MinimumPerimeter and MaximumPerimeter values define the range. |
| MinimumPerimeter | Double | Optional input Double that specifies the minimum perimeter value if the HolePatchType is specified to be kDerivedPatchRange. If not provided, an internal default value is assumed. |
| MaximumPerimeter | Double | Optional input Double that specifies the maximum perimeter value if the HolePatchType is specified to be kDerivedPatchRange. If not provided, an internal default value is assumed.   This is an optional argument whose default value is 0.0. |
| Reserved | Variant | Optional input Variant reserved for future use. Currently ignored.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Shrink wrap substitute in assembly](../../sample-programs/Shrinkwrap_Sample.md) | The following sample demonstrates the creation of a shrinkwrap substitute within an assembly. |

## Version

Introduced in version 2011
