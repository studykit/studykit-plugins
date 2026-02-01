# FilletVariableRadiusEdgeSet.ContinuityType Property

Parent Object: [FilletVariableRadiusEdgeSet](../FilletVariableRadiusEdgeSet/FilletVariableRadiusEdgeSet.md)

## Description

Read-write property that gets and sets the continuity type for the edge set. Valid values are kTangentContinuity and kCurvatureContinuity. This property can currently only be set in the forward create scenario (it fails if the FilletDefinition is obtained from an existing feature).

## Syntax

FilletVariableRadiusEdgeSet.**ContinuityType**() As [ContinuityTypeEnum](../ContinuityTypeEnum.md)

## Property Value

This is a read/write property whose value is a [ContinuityTypeEnum](../ContinuityTypeEnum.md).

## Version

Introduced in version 2012
