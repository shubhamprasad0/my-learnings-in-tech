# Installing Rust

- Doc: https://rust-book.cs.brown.edu/ch01-01-installation.html#installation
- `rustc --version` -- check rust version
- `rustup update` -- update rust version
- `rustup doc` -- offline doc
- `rustup doc --book` -- offline rust book

# Hello, world!

main.rs
```rust
fn main() {
    println!("Hello, world!")
}
```

- `rustc main.rs` to compile

# Hello, cargo

- `cargo new proj` -- to create new cargo project
- `cargo build` -- to build project
- `cargo run` -- to build and run
- `cargo build --release` -- to build optimized release version