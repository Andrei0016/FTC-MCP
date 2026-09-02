# `org.firstinspires.ftc.robotcore.external.matrices`

_ftc-sdk 11.1.0 — 10 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## class ColumnMajorMatrixF

```java
public abstract class org.firstinspires.ftc.robotcore.external.matrices.ColumnMajorMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.DenseMatrixF {
  public org.firstinspires.ftc.robotcore.external.matrices.ColumnMajorMatrixF(int, int);
  protected int indexFromRowCol(int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF toVector();
}
```

## class ColumnMatrixF

```java
public class org.firstinspires.ftc.robotcore.external.matrices.ColumnMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.MatrixF {
  public org.firstinspires.ftc.robotcore.external.matrices.ColumnMatrixF(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public float get(int, int);
  public void put(int, int, float);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF emptyMatrix(int, int);
}
```

## class DenseMatrixF

```java
public abstract class org.firstinspires.ftc.robotcore.external.matrices.DenseMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.MatrixF {
  protected org.firstinspires.ftc.robotcore.external.matrices.DenseMatrixF(int, int);
  public float get(int, int);
  public void put(int, int, float);
  public abstract float[] getData();
  protected abstract int indexFromRowCol(int, int);
}
```

## class GeneralMatrixF

```java
public class org.firstinspires.ftc.robotcore.external.matrices.GeneralMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.RowMajorMatrixF {
  public org.firstinspires.ftc.robotcore.external.matrices.GeneralMatrixF(int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.GeneralMatrixF(int, int, float[]);
  public float[] getData();
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF emptyMatrix(int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.GeneralMatrixF transposed();
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF transposed();
}
```

## class MatrixF

```java
public abstract class org.firstinspires.ftc.robotcore.external.matrices.MatrixF {
  protected int numRows;
  protected int numCols;
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF(int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.SliceMatrixF slice(int, int, int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.SliceMatrixF slice(int, int);
  public static org.firstinspires.ftc.robotcore.external.matrices.MatrixF identityMatrix(int);
  public static org.firstinspires.ftc.robotcore.external.matrices.MatrixF diagonalMatrix(int, float);
  public static org.firstinspires.ftc.robotcore.external.matrices.MatrixF diagonalMatrix(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public abstract org.firstinspires.ftc.robotcore.external.matrices.MatrixF emptyMatrix(int, int);
  public int numRows();
  public int numCols();
  public abstract float get(int, int);
  public abstract void put(int, int, float);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF getRow(int);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF getColumn(int);
  public java.lang.String toString();
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF transform(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  protected org.firstinspires.ftc.robotcore.external.matrices.VectorF adaptHomogeneous(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public java.lang.String formatAsTransform();
  public java.lang.String formatAsTransform(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF transposed();
  public void multiply(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF multiplied(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF multiplied(float);
  public void multiply(float);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF multiplied(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public void multiply(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF multiplied(float[]);
  public void multiply(float[]);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF toVector();
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF added(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public void add(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF subtracted(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public void subtract(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF added(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF added(float[]);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF subtracted(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF subtracted(float[]);
  public void add(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public void add(float[]);
  public void subtract(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public void subtract(float[]);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF getTranslation();
  protected java.lang.RuntimeException dimensionsError();
  protected static java.lang.RuntimeException dimensionsError(int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF inverted();
}
```

## class OpenGLMatrix

```java
public class org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix extends org.firstinspires.ftc.robotcore.external.matrices.ColumnMajorMatrixF {
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix();
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix(float[]);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF emptyMatrix(int, int);
  public static org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix rotation(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float, float);
  public static org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix rotation(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float);
  public static org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix translation(float, float, float);
  public static org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix identityMatrix();
  public float[] getData();
  public void scale(float, float, float);
  public void scale(float);
  public void translate(float, float, float);
  public void rotate(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float, float);
  public void rotate(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix scaled(float, float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix scaled(float);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix translated(float, float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix rotated(org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix rotated(org.firstinspires.ftc.robotcore.external.navigation.AxesReference, org.firstinspires.ftc.robotcore.external.navigation.AxesOrder, org.firstinspires.ftc.robotcore.external.navigation.AngleUnit, float, float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix inverted();
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix transposed();
  public org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix multiplied(org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF multiplied(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public void multiply(org.firstinspires.ftc.robotcore.external.matrices.OpenGLMatrix);
  public void multiply(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF inverted();
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF transposed();
}
```

## class RowMajorMatrixF

```java
public abstract class org.firstinspires.ftc.robotcore.external.matrices.RowMajorMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.DenseMatrixF {
  public org.firstinspires.ftc.robotcore.external.matrices.RowMajorMatrixF(int, int);
  protected int indexFromRowCol(int, int);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF toVector();
}
```

## class RowMatrixF

```java
public class org.firstinspires.ftc.robotcore.external.matrices.RowMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.MatrixF {
  public org.firstinspires.ftc.robotcore.external.matrices.RowMatrixF(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public float get(int, int);
  public void put(int, int, float);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF emptyMatrix(int, int);
}
```

## class SliceMatrixF

```java
public class org.firstinspires.ftc.robotcore.external.matrices.SliceMatrixF extends org.firstinspires.ftc.robotcore.external.matrices.MatrixF {
  protected org.firstinspires.ftc.robotcore.external.matrices.MatrixF matrix;
  protected int row;
  protected int col;
  public org.firstinspires.ftc.robotcore.external.matrices.SliceMatrixF(org.firstinspires.ftc.robotcore.external.matrices.MatrixF, int, int, int, int);
  public float get(int, int);
  public void put(int, int, float);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF emptyMatrix(int, int);
}
```

## class VectorF

```java
public class org.firstinspires.ftc.robotcore.external.matrices.VectorF {
  protected float[] data;
  public static org.firstinspires.ftc.robotcore.external.matrices.VectorF length(int);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF(float[]);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF(float);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF(float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF(float, float, float);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF(float, float, float, float);
  public float[] getData();
  public int length();
  public float get(int);
  public void put(int, float);
  public java.lang.String toString();
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF normalized3D();
  public float magnitude();
  public float dotProduct(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF multiplied(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF added(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF added(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public void add(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.MatrixF subtracted(org.firstinspires.ftc.robotcore.external.matrices.MatrixF);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF subtracted(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public void subtract(org.firstinspires.ftc.robotcore.external.matrices.VectorF);
  public org.firstinspires.ftc.robotcore.external.matrices.VectorF multiplied(float);
  public void multiply(float);
  protected java.lang.RuntimeException dimensionsError();
  protected static java.lang.RuntimeException dimensionsError(int);
}
```
