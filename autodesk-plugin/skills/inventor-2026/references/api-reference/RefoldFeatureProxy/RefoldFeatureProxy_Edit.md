# RefoldFeatureProxy.Edit Method

Parent Object: [RefoldFeatureProxy](../RefoldFeatureProxy/RefoldFeatureProxy.md)

## Description

Method that edits an existing refold feature. The stop node should be positioned immediately before this feature before calling this method so that all of the input is available and in a valid state.

## Syntax

RefoldFeatureProxy.**Edit**( ***StationaryFace*** As [Face](../Face/Face.md), [***Bends***] As Variant, [***Sketches***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StationaryFace | [Face](../Face/Face.md) | Input Face object that specifies the geometry that will remain fixed while other geometry refolds. See Remarks. |
| Bends | Variant | Optional input ObjectCollection that defines the bend(s) to refold. The bends specified must be in an unfolded state (IsFlat equals True). Not providing this argument or inputting Nothing indicates that all flat bends are to be refolded. |
| Sketches | Variant | Optional input ObjectCollection that specifies any sketches to be copied and transformed as part of the folding operation. The input sketches must be a child of one of the faces being folded. Also only one sketch per folded face is allowed.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
