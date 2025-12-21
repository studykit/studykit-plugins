# UnfoldFeatureProxy.Edit Method

Parent Object: [UnfoldFeatureProxy](../UnfoldFeatureProxy/UnfoldFeatureProxy.md)

## Description

Method that edits an existing unfold feature. The stop node should be positioned immediately before this feature before calling this method so that all of the input is available and in a valid state.

## Syntax

UnfoldFeatureProxy.**Edit**( ***StationaryFace*** As [Face](../Face/Face.md), [***Bends***] As Variant, [***Sketches***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StationaryFace | [Face](../Face/Face.md) | Input Face object that specifies the geometry that will remain fixed while other geometry unfolds. See Remarks. |
| Bends | Variant | Optional input ObjectCollection that defines the bend(s) to unfold. The bends specified must be in a folded state (IsFlat equals False). Not providing this argument or inputting Nothing indicates that all flat bends are to be unfolded. |
| Sketches | Variant | Optional input ObjectCollection that specifies any sketches to be copied and transformed as part of the unfolding operation. The input sketches must be a child of one of the faces being unfolded. Also only one sketch per unfolded face is allowed.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
