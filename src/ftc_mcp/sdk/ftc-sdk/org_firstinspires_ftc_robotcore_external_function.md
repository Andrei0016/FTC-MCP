# `org.firstinspires.ftc.robotcore.external.function`

_ftc-sdk 11.1.0 — 16 types. Signatures are exact (`javap -protected`); see `reference/ftc-sdk/` for decompiled bodies._

## interface Consumer

```java
public interface org.firstinspires.ftc.robotcore.external.function.Consumer<T> {
  public abstract void accept(T);
}
```

## class Continuation

```java
public class org.firstinspires.ftc.robotcore.external.function.Continuation<T> {
  public static final java.lang.String TAG;
  protected final T target;
  protected org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<T> dispatcher;
  public T getTarget();
  public org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<T> getDispatcher();
  protected org.firstinspires.ftc.robotcore.external.function.Continuation(T);
  public static <T> org.firstinspires.ftc.robotcore.external.function.Continuation<T> createTrivial(T);
  public static <T> org.firstinspires.ftc.robotcore.external.function.Continuation<T> create(java.util.concurrent.Executor, T);
  public static <T> org.firstinspires.ftc.robotcore.external.function.Continuation<T> create(android.os.Handler, T);
  public <U> org.firstinspires.ftc.robotcore.external.function.Continuation<U> createForNewTarget(U);
  public void dispatch(org.firstinspires.ftc.robotcore.external.function.ContinuationResult<? super T>);
  public void dispatchHere(org.firstinspires.ftc.robotcore.external.function.ContinuationResult<? super T>);
  public boolean isHandler();
  public android.os.Handler getHandler();
  public boolean isTrivial();
  public boolean isDispatchSynchronous();
  public boolean canBorrowThread(java.lang.Thread);
  protected org.firstinspires.ftc.robotcore.external.function.Continuation<T> createTrivialDispatcher();
  protected org.firstinspires.ftc.robotcore.external.function.Continuation<T> createHandlerDispatcher(android.os.Handler);
  protected org.firstinspires.ftc.robotcore.external.function.Continuation<T> createExecutorDispatcher(java.util.concurrent.Executor);
  protected org.firstinspires.ftc.robotcore.external.function.Continuation<T> setDispatcher(org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<T>);
}
```

## class Continuation.Dispatcher

```java
public abstract class org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<S> extends org.firstinspires.ftc.robotcore.internal.system.MemberwiseCloneable<org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<S>> {
  protected org.firstinspires.ftc.robotcore.external.function.Continuation<S> continuation;
  public org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher(org.firstinspires.ftc.robotcore.external.function.Continuation<S>);
  public boolean isTrivial();
  public boolean isHandler();
  public boolean isExecutor();
  public void setContinuation(org.firstinspires.ftc.robotcore.external.function.Continuation<S>);
  public abstract void dispatch(org.firstinspires.ftc.robotcore.external.function.ContinuationResult<? super S>);
  public <U> org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<U> copyAndCast();
}
```

## class Continuation.ExecutorDispatcher

```java
public class org.firstinspires.ftc.robotcore.external.function.Continuation.ExecutorDispatcher<S> extends org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<S> {
  public org.firstinspires.ftc.robotcore.external.function.Continuation.ExecutorDispatcher(org.firstinspires.ftc.robotcore.external.function.Continuation<S>, java.util.concurrent.Executor);
  public boolean isExecutor();
  public java.util.concurrent.Executor getExecutor();
  public void dispatch(org.firstinspires.ftc.robotcore.external.function.ContinuationResult<? super S>);
}
```

## class Continuation.HandlerDispatcher

```java
public class org.firstinspires.ftc.robotcore.external.function.Continuation.HandlerDispatcher<S> extends org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<S> {
  public org.firstinspires.ftc.robotcore.external.function.Continuation.HandlerDispatcher(org.firstinspires.ftc.robotcore.external.function.Continuation<S>, android.os.Handler);
  public boolean isHandler();
  public android.os.Handler getHandler();
  public void dispatch(org.firstinspires.ftc.robotcore.external.function.ContinuationResult<? super S>);
}
```

## class Continuation.TrivialDispatcher

```java
public class org.firstinspires.ftc.robotcore.external.function.Continuation.TrivialDispatcher<S> extends org.firstinspires.ftc.robotcore.external.function.Continuation.Dispatcher<S> {
  public org.firstinspires.ftc.robotcore.external.function.Continuation.TrivialDispatcher(org.firstinspires.ftc.robotcore.external.function.Continuation<S>);
  public boolean isTrivial();
  public void dispatch(org.firstinspires.ftc.robotcore.external.function.ContinuationResult<? super S>);
}
```

## interface ContinuationResult

```java
public interface org.firstinspires.ftc.robotcore.external.function.ContinuationResult<T> {
  public abstract void handle(T);
}
```

## interface Function

```java
public interface org.firstinspires.ftc.robotcore.external.function.Function<T, R> {
  public abstract R apply(T);
}
```

## interface InterruptableThrowingCallable

```java
public interface org.firstinspires.ftc.robotcore.external.function.InterruptableThrowingCallable<VALUE, EXCEPTION extends java.lang.Throwable> {
  public abstract VALUE call() throws EXCEPTION, java.lang.InterruptedException;
}
```

## interface InterruptableThrowingRunnable

```java
public interface org.firstinspires.ftc.robotcore.external.function.InterruptableThrowingRunnable<EXCEPTION extends java.lang.Throwable> {
  public abstract void run() throws EXCEPTION, java.lang.InterruptedException;
}
```

## interface InterruptableThrowingSupplier

```java
public interface org.firstinspires.ftc.robotcore.external.function.InterruptableThrowingSupplier<VALUE, EXCEPTION extends java.lang.Throwable> {
  public abstract VALUE get() throws EXCEPTION, java.lang.InterruptedException;
}
```

## interface Predicate

```java
public interface org.firstinspires.ftc.robotcore.external.function.Predicate<T> {
  public abstract boolean test(T);
}
```

## interface Supplier

```java
public interface org.firstinspires.ftc.robotcore.external.function.Supplier<T> {
  public abstract T get();
}
```

## interface ThrowingCallable

```java
public interface org.firstinspires.ftc.robotcore.external.function.ThrowingCallable<VALUE, EXCEPTION extends java.lang.Throwable> {
  public abstract VALUE call() throws EXCEPTION;
}
```

## interface ThrowingRunnable

```java
public interface org.firstinspires.ftc.robotcore.external.function.ThrowingRunnable<EXCEPTION extends java.lang.Throwable> {
  public abstract void run() throws EXCEPTION;
}
```

## interface ThrowingSupplier

```java
public interface org.firstinspires.ftc.robotcore.external.function.ThrowingSupplier<VALUE, EXCEPTION extends java.lang.Throwable> {
  public abstract VALUE get() throws EXCEPTION;
}
```
