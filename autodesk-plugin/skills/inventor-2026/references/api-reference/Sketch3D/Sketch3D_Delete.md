# Sketch3D.Delete Method

Parent Object: [Sketch3D](../Sketch3D/Sketch3D.md)

## Description

Method that deletes the 3D sketch. This method will fail in the cases where the sketch is active, and when there are dependents on the sketch. In the cases where other geometry, besides a feature, is dependent on the sketch, the dependent geometry will be deleted or modified.

## Syntax

Sketch3D.**Delete**()

## Version

Introduced in version 6
