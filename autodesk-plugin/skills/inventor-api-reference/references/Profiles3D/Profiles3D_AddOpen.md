# Profiles3D.AddOpen Method

Parent Object: [Profiles3D](../Profiles3D/Profiles3D.md)

## Description

Method that creates a new profile by examining the contents of the sketch for a set of connected entities and creating as many paths as possible. The paths may be open or closed. The resulting Profile3D is returned.

## Syntax

Profiles3D.**AddOpen**() As [Profile3D](../Profile3D/Profile3D.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |

## Version

Introduced in version 6
